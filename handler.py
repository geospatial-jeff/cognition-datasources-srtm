from datasources import Manifest

def DGOpenData(event, context):
    manifest = Manifest()
    manifest['DGOpenData'].search(**event)
    response = manifest.execute()
    return response