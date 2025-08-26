from xml.dom import minidom
from flask import jsonify

def nf_data(bar_code):

    xml = minidom.parse(open(f'files/{bar_code}-nfe.xml'))
    products = []

    # NFe products
    itens = xml.getElementsByTagName('det')

    for item in itens:
        sku = item.getElementsByTagName('cProd')[0].firstChild.data
        qty = item.getElementsByTagName('qCom')[0].firstChild.data
        product_name = item.getElementsByTagName('xProd')[0].firstChild.data

        product = {
            'sku': sku,
            'qty': qty,
            'product_name': product_name            
        }
        products.append(product)     

    num_NF = xml.getElementsByTagName('ide')[0].getElementsByTagName('nNF')[0].firstChild.data
    customer = xml.getElementsByTagName('dest')[0].getElementsByTagName('xNome')[0].firstChild.data

    response = jsonify({
        'customer': customer,
        'num_nf': num_NF,        
        'products': products
        })       

    return response
