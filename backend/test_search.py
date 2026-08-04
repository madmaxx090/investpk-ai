from app.services.psx_service import PSXService

psx = PSXService()

print(psx.search_company("hubc"))
print(psx.search_company("HUBC"))
print(psx.search_company("engro"))
print(psx.search_company("bank"))