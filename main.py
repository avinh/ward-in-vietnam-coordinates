import pandas as pd
import json
import requests

df = pd.read_csv('input.csv', dtype={'Mã PX': str}, encoding='utf-8')

base_search_url = "https://autosuggest.search.hereapi.com/v1/autosuggest"

hierarchical_data = {}

def get_coordinates(phuong_xa):
    params = {
        "xnlp": "CL_JSMv3.1.54.1",
        "apikey": "qsmBCzGufS4nWKvuFiGW33nhrsYtvqPhNRScDsktRgw",
        "at": "52.5,13.4",
        "lang": "vi-VN",
        "politicalView": "VNM",
        "limit": 1,
        "q": phuong_xa
    }

    headers = {
        "Referer": "https://wego.here.com",
        "Origin": "https://wego.here.com/"
    }
    
    response = requests.get(base_search_url, params=params, headers=headers)
    if response.status_code == 200:
        content = response.json()
        return content["items"][0]['position']['lat'], content["items"][0]['position']['lng']
    
    return None, None

for i, row in df.iterrows():
    tp = row['Tỉnh Thành Phố']
    qh = row['Quận Huyện']
    px = row['Phường Xã']
    ma_px = row['Mã PX']
    ma_qh = row['Mã QH']
    ma_tp = row['Mã TP']
    
    address = f"{px}, {qh}, {tp}, Vietnam"
    
    lat, lng = get_coordinates(address)
    
    if tp not in hierarchical_data:
        hierarchical_data[tp] = {
            'ma_tp': ma_tp
        }
    
    if qh not in hierarchical_data[tp]:
        hierarchical_data[tp][qh] = {
            'ma_qh': ma_qh
        }
    
    hierarchical_data[tp][qh][px] = {
        'ma_px': ma_px,
        'lat': lat,
        'lng': lng
    }

    print(i, address, lat, lng)

json_data = json.dumps(hierarchical_data, ensure_ascii=False, indent=4)

with open('output.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print("done")
