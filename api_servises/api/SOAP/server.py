from flask import Flask, request, Response
from lxml import etree

app = Flask(__name__)

WSDL_PATH = "calculator.wsdl"
TNS = "http://example.com/calculator"

SOAPENV_NS = "http://schemas.xmlsoap.org/soap/envelope/"
NSMAP = {
    "soapenv": SOAPENV_NS,
    "tns": TNS,
}

def soap_fault(code: str, message: str, http_status: int = 500) -> Response:
    # SOAP 1.1 Fault
    envelope = etree.Element(etree.QName(SOAPENV_NS, "Envelope"), nsmap=NSMAP)
    body = etree.SubElement(envelope, etree.QName(SOAPENV_NS, "Body"))
    fault = etree.SubElement(body, "Fault")  # Fault обычно без namespace в SOAP 1.1 ответах
    faultcode = etree.SubElement(fault, "faultcode")
    faultcode.text = code
    faultstring = etree.SubElement(fault, "faultstring")
    faultstring.text = message

    xml = etree.tostring(envelope, xml_declaration=True, encoding="utf-8")
    return Response(xml, status=http_status, content_type="text/xml; charset=utf-8")

def soap_response(body_element: etree._Element) -> Response:
    envelope = etree.Element(etree.QName(SOAPENV_NS, "Envelope"), nsmap=NSMAP)
    body = etree.SubElement(envelope, etree.QName(SOAPENV_NS, "Body"))
    body.append(body_element)

    xml = etree.tostring(envelope, xml_declaration=True, encoding="utf-8")
    return Response(xml, status=200, content_type="text/xml; charset=utf-8")


@app.get("/wsdl")
def wsdl():
    with open(WSDL_PATH, "rb") as f:
        return Response(f.read(), content_type="text/xml; charset=utf-8")


@app.post("/wsdl")
def handle_soap():
    raw = request.data
    if not raw:
        return soap_fault("Client", "Empty request body", 400)

    try:
        root = etree.fromstring(raw)
    except Exception as e:
        return soap_fault("Client", f"Invalid XML: {e}", 400)

    body = root.find(".//{http://schemas.xmlsoap.org/soap/envelope/}Body")
    if body is None or len(body) == 0:
        return soap_fault("Client", "SOAP Body not found", 400)

    # Внутри Body первый элемент — это операция/запрос (AddRequest или HelloRequest)
    op = body[0]
    local = etree.QName(op).localname

    if local == "AddRequest":
        a_el = op.find(f"{{{TNS}}}a")
        b_el = op.find(f"{{{TNS}}}b")
        try:
            a = int(a_el.text) if a_el is not None else 0
            b = int(b_el.text) if b_el is not None else 0
        except Exception:
            return soap_fault("Client", "a and b must be integers", 400)

        # Формируем ответ AddResponse
        resp = etree.Element(etree.QName(TNS, "AddResponse"), nsmap={"tns": TNS})
        res_el = etree.SubElement(resp, etree.QName(TNS, "result"))
        res_el.text = str(a + b)
        return soap_response(resp)

    if local == "HelloRequest":
        name_el = op.find(f"{{{TNS}}}name")
        name = (name_el.text or "").strip() if name_el is not None else ""
        if not name:
            name = "world"

        resp = etree.Element(etree.QName(TNS, "HelloResponse"), nsmap={"tns": TNS})
        g_el = etree.SubElement(resp, etree.QName(TNS, "greeting"))
        g_el.text = f"Hello, {name}!"
        return soap_response(resp)

    return soap_fault("Client", f"Unknown operation: {local}", 400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

