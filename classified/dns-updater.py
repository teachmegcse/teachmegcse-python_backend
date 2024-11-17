from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')

url = "https://api.cloudflare.com/client/v4/zones/b86a9622145da726c38802379ea1ecd9/dns_records/74a60e0471c24616896c39d375e538b7"
print(ip)
payload = {
    "content": ip,
    "name": "api.teachmegcse.com",
    "proxied": False,
    "type": "A",
    "comment": "Domain verification record",
    "id": "5e5a599c264e25b68bf8179081046a1ddf8bd",
    "tags": [],
    "ttl": 60
}
headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": ""
}
