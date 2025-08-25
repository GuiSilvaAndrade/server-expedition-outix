from xml.dom import minidom

def nf_data(bar_code):

    xml = minidom.parse(open(f'files/{bar_code}-nfe.xml'))
    
    num_NF = xml.getElementsByTagName('ide')[0].getElementsByTagName('nNF')[0].firstChild.data
    customer = xml.getElementsByTagName('dest')[0].getElementsByTagName('xNome')[0].firstChild.data 

    # NFe itens
    itens = xml.getElementsByTagName('det')
    sku, qty, product = [], [], []
    for item in itens:
        sku.append(item.getElementsByTagName('cProd')[0].firstChild.data)
        qty.append(item.getElementsByTagName('qCom')[0].firstChild.data)
        product.append(item.getElementsByTagName('xProd')[0].firstChild.data)

    return customer, num_NF, product, qty
