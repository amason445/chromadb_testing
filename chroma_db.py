import chromadb
from faker import Faker
import json

import ef_functions

client = chromadb.Client()

test_collection = client.get_or_create_collection(name = "test_collection", embedding_function= ef_functions.openai_ef)

fake = Faker()
number_of_records = 100

#write to db with embeddings
for i in range(1, number_of_records + 1):

    id_string = "id_" + str(i)

    test_collection.add(
        documents=[fake.text()],
        metadatas= {"recipient": fake.email(), "sender": fake.email(), "subject":fake.sentence(), "sent_on": str(fake.date_between(start_date = '-1y', end_date = 'today'))},
        ids= [id_string]
    )

#get by id and write to json
for i in range(1, number_of_records + 1):
    id_string = "id_" + str(i)

    id_query = test_collection.get(
        ids=[id_string],
        include= ['embeddings','metadatas','documents']
    )

    output_json = json.dumps(id_query, indent=4)

    with open('test_collections_json/' + id_string + '.json', "w") as f:
        f.write(output_json)
        f.close()

client.delete_collection(name="test_collection")


