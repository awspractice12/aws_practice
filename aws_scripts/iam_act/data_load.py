import json

def parse_jsonfl(file_path):
    with open(file_path) as file_object:
            # store file data in object
            data = json.load(file_object)
            # for load_item in data["Statement"]:
            #     print(load_item)
            print(data)
            return data

# parse_jsonfl("D:\\awscli\\pyaut\\iam_act\\jsons\\first_managed_policy.json")