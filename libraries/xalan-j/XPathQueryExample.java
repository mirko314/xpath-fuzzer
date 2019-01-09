import java.io.StringWriter;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Node;

// import javax.xml.parsers.DocumentBuilder;
// import javax.xml.parsers.DocumentBuilderFactory;
// import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

// import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
// import org.xml.sax.SAXException;

public class XPathQueryExample {

  public static void main(String[] args) {
    DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    factory.setNamespaceAware(true);
    DocumentBuilder builder;
    Document doc = null;
    try {
      String file_name = args[0];
      String XPath_expression = args[1];
      builder = factory.newDocumentBuilder();
      doc = builder.parse(file_name);

      // Create XPathFactory object
      XPathFactory xpathFactory = XPathFactory.newInstance();

      // Create XPath object
      XPath xpath = xpathFactory.newXPath();
      XPathExpression expr = xpath.compile(XPath_expression);
      // Object result = expr.evaluate(doc);
      try {
          NodeList nodeList = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
          for (int i = 0; i < nodeList.getLength(); i++) {
              Node node = nodeList.item(i);
              System.out.println(nodeToString(node));
          }
      } catch (XPathExpressionException e) {
          String result = expr.evaluate(doc);
          System.out.println(result);
      }
      // if (result instanceof NodeList) {
      //   NodeList nodes = (NodeList) result;
      //   for (int i = 0; i < nodes.getLength(); i++) {
      //     System.out.println(nodeToString(nodes.item(i)));
      //   }
      // }
      // else {
      //   System.out.println(result);
      // }
      // } catch (ParserConfigurationException | Exception | SAXException |
      // XPathExpressionException | IOException e) {
    } catch (Exception e) {
      e.printStackTrace();
    }

  }

  private static String nodeToString(Node node) throws Exception {
    StringWriter sw = new StringWriter();

    Transformer t = TransformerFactory.newInstance().newTransformer();
    t.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
    t.setOutputProperty(OutputKeys.INDENT, "yes");
    t.transform(new DOMSource(node), new StreamResult(sw));

    return sw.toString();
  }

}
