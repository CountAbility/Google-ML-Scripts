from google.cloud import vision

client = vision.ImageAnnotatorClient()
response = client.annotate_image({
  'image': {'source': {'image_uri': 'https://images.unsplash.com/photo-1522556189639-b150ed9c4330?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fHBlb3BsZSUyMHNtaWxlfGVufDB8fDB8fHww&w=1000&q=80'}},
  'features': [{'type_': vision.Feature.Type.FACE_DETECTION}]
})

print(response)