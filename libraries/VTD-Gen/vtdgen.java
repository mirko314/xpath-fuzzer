//https://vtd-xml.sourceforge.io/codeSample/RSSReader2.java
//https://vtd-xml.sourceforge.io/codeSample/cs1.html

/*
 * Copyright (C) 2002-2011 XimpleWare, info@ximpleware.com
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */

/*This is the XPath version of RSSReader
 */
import com.ximpleware.*;
import com.ximpleware.xpath.*;
import java.io.*;
import java.util.*;

public class vtdgen {

  public static void main(String argv[]) {
    try {
      String file_name = argv[0];
      String XPath_expression = argv[1];
      // open a file and read the content into a byte array
      File f = new File(file_name);
      FileInputStream fis = new FileInputStream(f);
      byte[] b = new byte[(int) f.length()];
      fis.read(b);
      // instantiate VTDGen
      // and call parse
      VTDGen vg = new VTDGen();
      vg.setDoc(b);
      vg.parse(true); // set namespace awareness to true
      VTDNav vn = vg.getNav();
      AutoPilot ap = new AutoPilot(vn);
      ap.declareXPathNameSpace("a", "https://a.com/");
      ap.declareXPathNameSpace("b", "https://b.com/");
      ap.declareXPathNameSpace("c", "https://c.com/");
      ap.declareXPathNameSpace("d", "https://d.com/");
      ap.declareXPathNameSpace("e", "https://e.com/");
      ap.selectXPath(XPath_expression);

      FastLongBuffer flb = new FastLongBuffer(4);
      int i;
      byte[] xml = vn.getXML().getBytes();
      try {
        while( (i=ap.evalXPath())!= -1){
            flb.append(vn.getElementFragment());
        }
      } catch (XPathEvalException e) {
        ap.resetXPath();
        System.out.print(ap.evalXPathToString());
        return;
      } catch (NavException e) {
        // This is for Attribute selection. getElementFragment does not work then.
        // However this does only return the first result / first attribute value
        ap.resetXPath();
        System.out.print(ap.evalXPathToString());
        return;

      }
      int size = flb.size();
      if (size != 0) {
        for (int k = 0; k < size; k++) {
          ByteArrayOutputStream fos = new ByteArrayOutputStream();
          fos.write(xml, flb.lower32At(k), flb.upper32At(k));
          System.out.print(fos.toString("UTF-8"));
        }

      }

    } catch (Exception e) {
      e.printStackTrace();

    }
  }
}