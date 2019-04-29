from datasources import Manifest

def SRTM(event, context):
    manifest = Manifest()
    manifest['SRTM'].search(**event)
    response = manifest.execute()
    return response
