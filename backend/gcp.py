from re import M
from google.cloud import language_v1

from settings import GOOGLE_APPLICATION_CREDENTIALS
from collections import Counter, OrderedDict

def analyze_text_using_gcp(text_content):

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
    org_dict = {}
    date = None
    mvp_org = None
    location = None

    # Loop through entitites returned from the API
    for entity in response.entities:
        # print(u"Representative name for the entity: {}".format(entity.name))

        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        # print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))
        entity_type = language_v1.Entity.Type(entity.type_).name
        if entity_type == 'ORGANIZATION':
            org_dict[entity.name] = entity.salience
        if entity_type == 'DATE' and 'year' in entity.metadata and 'month' in entity.metadata and 'day' in entity.metadata: 
            date = entity.name
        if entity_type == 'LOCATION':
            location = entity.name
        # Get the salience score associated with the entity in the [0, 1.0] range
        # print(u"Salience score: {}".format(entity.salience))

        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        # for metadata_name, metadata_value in entity.metadata.items():
        #     print(u"{}: {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        # for mention in entity.mentions:
        #     print(u"Mention text: {}".format(mention.text.content))

        #     # Get the mention type, e.g. PROPER for proper noun
        #     print(
        #         u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
        #     )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    # print(u"Language of the text: {}".format(response.language))
    if len(org_dict) > 0 :
        d_descending = sorted(org_dict.items(), key=lambda kv: kv[1], reverse=True)[0][0]
        mvp_org = d_descending
    return {
        'organization': mvp_org,
        'date': date,
        'location' : location
    }
