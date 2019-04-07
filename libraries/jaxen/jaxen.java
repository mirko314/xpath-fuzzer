
/*
 * $Header$
 * $Revision$
 * $Date$
 *
 * ====================================================================
 *
 * Copyright 2000-2002 bob mcwhirter & James Strachan.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 *   * Neither the name of the Jaxen Project nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
 * IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
 * TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
 * PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
 * OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * ====================================================================
 * This software consists of voluntary contributions made by many
 * individuals on behalf of the Jaxen Project and was originally
 * created by bob mcwhirter <bob@werken.com> and
 * James Strachan <jstrachan@apache.org>.  For more information on the
 * Jaxen Project, please see <http://www.jaxen.org/>.
 *
 * $Id$
 */

import java.io.StringWriter;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Node;

import org.jaxen.dom.DOMXPath;

import org.jaxen.XPath;
import org.jaxen.JaxenException;
import org.jaxen.Navigator;
import org.jaxen.dom.DocumentNavigator;
import org.jaxen.function.StringFunction;
import org.jaxen.SimpleNamespaceContext;

import java.util.HashMap;

import java.util.List;
import java.util.Iterator;

public class jaxen {
  public static void main(String[] args) {
    if (args.length != 2) {
      System.err.println("usage: DOMDemo <document url> <xpath expr>");
      System.exit(1);
    }

    try {
      DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
      factory.setNamespaceAware(true);
      DocumentBuilder builder = factory.newDocumentBuilder();

      Document doc = builder.parse(args[0]);

      HashMap namespaceMap = new HashMap();
      namespaceMap.put( "a", "https://a.com/");
      namespaceMap.put( "b", "https://b.com/");
      namespaceMap.put( "c", "https://c.com/");
      namespaceMap.put( "d", "https://d.com/");
      namespaceMap.put( "e", "https://e.com/");

      XPath xpath = new DOMXPath(args[1]);
      xpath.setNamespaceContext(new SimpleNamespaceContext(namespaceMap));
      Navigator navigator = xpath.getNavigator();

      // System.out.println("XPah:h " + xpath);
      Object res_obj = xpath.evaluate(doc);;
      try {
        List results = (List) res_obj;

      Iterator resultIter = results.iterator();

      // System.out.println("Document :: " + args[0]);
      // System.out.println("   XPath :: " + args[1]);
      // System.out.println("");
      // System.out.println("Results");
      // System.out.println("----------------------------------");
        while (resultIter.hasNext()) {
          Node result = (Node) resultIter.next();
          // String value = StringFunction.evaluate(result, navigator);
          System.out.println(nodeToString(result));
        }
      } catch (java.lang.ClassCastException ex) {
        System.out.println(res_obj);
      }
    } catch (JaxenException e) {
      e.printStackTrace();
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