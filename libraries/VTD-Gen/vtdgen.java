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
      ap.declareXPathNameSpace("ns1", "http://purl.org/dc/elements/1.1/");
      ap.selectXPath(XPath_expression);

      FastLongBuffer flb = new FastLongBuffer(4);
      int i;
      byte[] xml = vn.getXML().getBytes();
      while( (i=ap.evalXPath())!= -1){
          flb.append(vn.getElementFragment());
      }
      int size = flb.size();
      if (size != 0){
          for (int k = 0;k<size; k++){
              ByteArrayOutputStream fos = new ByteArrayOutputStream();
              fos.write(xml, flb.lower32At(k), flb.upper32At(k));
              System.out.print(fos.toString( "UTF-8" ));
          }

      }
    } catch (ParseException e) {
      System.out.println(" XML file parsing error \n" + e);
    } catch (NavException e) {
      System.out.println(" Exception during navigation " + e);
    } catch (XPathParseException e) {

    } catch (XPathEvalException e) {

    } catch (java.io.IOException e) {
      System.out.println(" IO exception condition" + e);
    }
  }
}