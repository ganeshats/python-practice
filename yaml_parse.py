import yaml

with open("dummy.yaml" , "r") as yml:
    yaml_var = yaml.load(yml)

print yaml_var
for ky in yaml_var:
    print "key: {0}, value = {1}".format(ky, yaml_var[ky])