import requests
import _csv

datas =[]
no = 0
page=0
for p in range(1,4):
      url = 'https://api.bukalapak.com/multistrategy-products?assurance=false&category_id=8&category_name=HP%20%26%20Smartphone&cities=&condition=&deal=false&facet=true&free_shipping_provinces=&from=omnisearch&from_keyword_history=false&installment=false&keywords=iphone&limit=30&offset=0&page='+str(p)+'&premium_seller=false&price_range=%3A&provinces=&sort=&store_id=&top_seller=false&wholesale=false&access_token=duIxIq0Zdk5E2dJcrNwXmQjJ8YguEMdnq7xgzsKHgia3bg'
      json_data = requests.get(url).json()
      print(json_data)
      # products = json_data['data']
      # print(len(products))
      # print(products)
      # page +=1
      # print(page)
      # for p in products:
      #       no+=1
      #       name = p['name']
      #       price = p['price']
            # rating = p['rating']['average_rate']
            # status= p['state']
            # spesifikasi = p['specs']
            # fitur = p['specs']['features']
            # merk = p['specs']['brand']
            # camera = p['specs']['camera']
            # resolusi_kamera = p['specs']['camera-resolution']
            # ukuran_layar = p['specs']['display_size']
            # memori = p['specs']['memory-size']
            # network = p['specs']['network']
            # os = p['specs']['operating_system']
            # prosesor = p['specs']['processor']
            # rasio = p['specs']['screen-aspect-ratio']
            # tipe_screen = p['specs']['screen-type']
            # sim = p['specs']['sim-card']
            # stok = p['stock']
            # nama_toko = p['store']['name']
            # id = p['store']['id']
            # alamat_toko = p['store']['address']['city']
            # print(name)
            # print(merk)
            # print(price)
            # print(rating)
            # print(status)
            # print(camera)
            # print(resolusi_kamera)
            # print(ukuran_layar)
            # # print(memori)
            # print(network)
            # print(os)
            # print(prosesor)
            # print(rasio)
            # print(sim)
            # print(stok)
            # print(nama_toko)
            # print(id)
            # print(alamat_toko)
            # print(no)
            # # datas.append([no,name,price,rating,status,ukuran_layar,network,os,prosesor,rasio,sim,stok,nama_toko,id,alamat_toko])
#
# with open('resultbukalapak', 'w', newline='') as file:
#       writer = _csv.writer(file)
#       headers = [
#             'Num','Name', 'Price', 'Rate', 'State', 'Display Size', 'Network', 'OS', 'Processor', 'Ratio','SIM Card','Stock','Store Name','Store ID', 'Store Address'
#       ]
#       writer.writerow(headers)
#       for data in datas:
#             writer.writerow(data)