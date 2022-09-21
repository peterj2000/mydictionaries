

codes={'A':'%','a':'9','B':'@','b':'#','C':'1','c':'2','D':'3','d':'4','E':'5','e':'6','F':'7','f':'8','G':')'
    ,'g':'(','H':'-','h':'*','I':'&','i':'^','J':'$','j':'#','K':'!','k':'@','L':'}','l':'{','M':'[','m':']','N':'?'
    ,'n':'/','O':'>','o':'<','P':'.','p':',','Q':'=','q':'+','R':'_','r':'|','S':'\\','s':'$','T':'€',
    't':'¢','U':'₹','u':'₱','V':'฿','v':'α','W':'β','w':'γ','X':'ε','x':'θ','Y':'κ','y':'μ','Z':'ξ',
    'z':'π'}


def convert(var):
    file_enc =""

    for x in var:
        get_codes =codes.get(x,None)
        if get_codes is None:
            

            file_enc += x
        else:
           
            file_enc += get_codes
        
    return file_enc
    



def main():
    file_name = input("Enter Filename:")


    with open(file_name) as a:
      infile = open('encrypted.txt',"w")

      for line in a:
        con_line = convert(line)
        infile.write(con_line)
      infile.close()


main()