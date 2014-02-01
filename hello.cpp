/*
 * =====================================================================================
 *
 *       Filename:  hello.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  02/01/2014 09:54:33 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Jie Feng (http://hey.i-feng.org/), jiefeng.hopkins@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */

#include <iostream>
using namespace std;
 
int main ()
{
    
   cout << "Content-type:text/html\r\n\r\n";
   cout << "<html>\n";
   cout << "<head>\n";
   cout << "<title>Hello World - First CGI Program</title>\n";
   cout << "</head>\n";
   cout << "<body>\n";
   cout << "<h2>Hello World! This is my first CGI program</h2>\n";
   cout << "</body>\n";
   cout << "</html>\n";
   
   return 0;
}
