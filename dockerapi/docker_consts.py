"""
Constant values taken from https://docs.docker.com/engine/api/v1.41/ and returned based on API requests
"""

from dockerapi import utils

util = utils.Utils()

API_VERSION = '''
{
  "Platform": {
    "Name": "Linux"
  },
  "Components": [
    {
      "Name": "Engine",
      "Version": "19.03.12",
      "Details": {}
    }
  ],
  "Version": "19.03.12",
  "ApiVersion": "1.40",
  "MinAPIVersion": "1.12",
  "GitCommit": "48a66213fe",
  "GoVersion": "go1.13.14",
  "Os": "linux",
  "Arch": "amd64",
  "KernelVersion": "4.19.76-linuxkit",
  "Experimental": true,
  "BuildTime": "2021-05-01T15:49:27.000000000+00:00"
}\n
'''

API_RESP_IMAGES_JSON_LIST = '''
[
  {
    "Id": "sha256:e216a057b1cb1efc11f8a268f37ef62083e70b1b38323ba252e25ac88904a7e8",
    "ParentId": "",
    "RepoTags": [
      "ubuntu:12.04",
      "ubuntu:precise"
    ],
    "RepoDigests": [
      "ubuntu@sha256:992069aee4016783df6345315302fa59681aae51a8eeb2f889dea59290f21787"
    ],
    "Created": 1474925151,
    "Size": 103579269,
    "VirtualSize": 103579269,
    "SharedSize": 0,
    "Labels": {},
    "Containers": 2
  },
  {
    "Id": "sha256:3e314f95dcace0f5e4fd37b10862fe8398e3c60ed36600bc0ca5fda78b087175",
    "ParentId": "",
    "RepoTags": [
      "ubuntu:12.10",
      "ubuntu:quantal"
    ],
    "RepoDigests": [
      "ubuntu@sha256:002fba3e3255af10be97ea26e476692a7ebed0bb074a9ab960b2e7a1526b15d7",
      "ubuntu@sha256:68ea0200f0b90df725d99d823905b04cf844f6039ef60c60bf3e019915017bd3"
    ],
    "Created": 1403128455,
    "Size": 172064416,
    "VirtualSize": 172064416,
    "SharedSize": 0,
    "Labels": {},
    "Containers": 5
  }
]\n
'''

API_RESP_CONTAINERS_JSON_LIST = '''[
  {
    "Id": "8dfafdbc3a40",
    "Names": [
      "/boring_feynman"
    ],
    "Image": "ubuntu:latest",
    "ImageID": "d74508fb6632491cea586a1fd7d748dfc5274cd6fdfedee309ecdcbc2bf5cb82",
    "Command": "echo 1",
    "Created": 1367854155,
    "State": "Exited",
    "Status": "Exit 0",
    "Ports": [
      {
        "PrivatePort": 2222,
        "PublicPort": 3333,
        "Type": "tcp"
      }
    ],
    "Labels": {
      "com.prod.vendor": "Prod",
      "com.prod.license": "Apache",
      "com.prod.version": "1.0"
    },
    "SizeRw": 12288,
    "SizeRootFs": 0,
    "HostConfig": {
      "NetworkMode": "default"
    },
    "NetworkSettings": {
      "Networks": {
        "bridge": {
          "NetworkID": "7ea29fc1412292a2d7bba362f9253545fecdfa8ce9a6e37dd10ba8bee7129812",
          "EndpointID": "2cdc4edb1ded3631c81f57966563e5c8525b81121bb3706a9a9a3ae102711f3f",
          "Gateway": "172.17.0.1",
          "IPAddress": "172.17.0.2",
          "IPPrefixLen": 16,
          "IPv6Gateway": "",
          "GlobalIPv6Address": "",
          "GlobalIPv6PrefixLen": 0,
          "MacAddress": "02:42:ac:11:00:02"
        }
      }
    },
    "Mounts": [
      {
        "Name": "fac362...80535",
        "Source": "/data",
        "Destination": "/data",
        "Driver": "local",
        "Mode": "ro,Z",
        "RW": false,
        "Propagation": ""
      }
    ]
  },
  {
    "Id": "9cd87474be90",
    "Names": [
      "/prod"
    ],
    "Image": "ubuntu:latest",
    "ImageID": "d74508fb6632491cea586a1fd7d748dfc5274cd6fdfedee309ecdcbc2bf5cb82",
    "Command": "echo 222222",
    "Created": 1367854155,
    "State": "Exited",
    "Status": "Exit 0",
    "Ports": [],
    "Labels": {},
    "SizeRw": 12288,
    "SizeRootFs": 0,
    "HostConfig": {
      "NetworkMode": "default"
    },
    "NetworkSettings": {
      "Networks": {
        "bridge": {
          "NetworkID": "7ea29fc1412292a2d7bba362f9253545fecdfa8ce9a6e37dd10ba8bee7129812",
          "EndpointID": "88eaed7b37b38c2a3f0c4bc796494fdf51b270c2d22656412a2ca5d559a64d7a",
          "Gateway": "172.17.0.1",
          "IPAddress": "172.17.0.8",
          "IPPrefixLen": 16,
          "IPv6Gateway": "",
          "GlobalIPv6Address": "",
          "GlobalIPv6PrefixLen": 0,
          "MacAddress": "02:42:ac:11:00:08"
        }
      }
    },
    "Mounts": []
  },
  {
    "Id": "3176a2479c92",
    "Names": [
      "/sleepy_dog"
    ],
    "Image": "ubuntu:latest",
    "ImageID": "d74508fb6632491cea586a1fd7d748dfc5274cd6fdfedee309ecdcbc2bf5cb82",
    "Command": "echo 3333333333333333",
    "Created": 1367854154,
    "State": "Exited",
    "Status": "Exit 0",
    "Ports": [],
    "Labels": {},
    "SizeRw": 12288,
    "SizeRootFs": 0,
    "HostConfig": {
      "NetworkMode": "default"
    },
    "NetworkSettings": {
      "Networks": {
        "bridge": {
          "NetworkID": "7ea29fc1412292a2d7bba362f9253545fecdfa8ce9a6e37dd10ba8bee7129812",
          "EndpointID": "8b27c041c30326d59cd6e6f510d4f8d1d570a228466f956edf7815508f78e30d",
          "Gateway": "172.17.0.1",
          "IPAddress": "172.17.0.6",
          "IPPrefixLen": 16,
          "IPv6Gateway": "",
          "GlobalIPv6Address": "",
          "GlobalIPv6PrefixLen": 0,
          "MacAddress": "02:42:ac:11:00:06"
        }
      }
    },
    "Mounts": []
  },
  {
    "Id": "4cb07b47f9fb",
    "Names": [
      "/running_cat"
    ],
    "Image": "ubuntu:latest",
    "ImageID": "d74508fb6632491cea586a1fd7d748dfc5274cd6fdfedee309ecdcbc2bf5cb82",
    "Command": "echo 444444444444444444444444444444444",
    "Created": 1367854152,
    "State": "Exited",
    "Status": "Exit 0",
    "Ports": [],
    "Labels": {},
    "SizeRw": 12288,
    "SizeRootFs": 0,
    "HostConfig": {
      "NetworkMode": "default"
    },
    "NetworkSettings": {
      "Networks": {
        "bridge": {
          "NetworkID": "7ea29fc1412292a2d7bba362f9253545fecdfa8ce9a6e37dd10ba8bee7129812",
          "EndpointID": "d91c7b2f0644403d7ef3095985ea0e2370325cd2332ff3a3225c4247328e66e9",
          
          "Gateway": "172.17.0.1",
          "IPAddress": "172.17.0.5",
          "IPPrefixLen": 16,
          "IPv6Gateway": "",
          "GlobalIPv6Address": "",
          "GlobalIPv6PrefixLen": 0,
          "MacAddress": "02:42:ac:11:00:05"
        }
      }
    },
    "Mounts": []
  }
]"\n
'''

API_RESP_CONTAINERS_JSON_CREATE = ('''{
    "Id": "%s",
    "Warnings": []
}''' % util.gen_container_id())

API_RESP_CONTAINERS_JSON_CREATE_NO_SUCH_CONTAINER = '''{
    "message": "No such container"
}\n
'''


API_SOMETHING_WENT_WRONG = '''{
    "message" : "something went wrong"
}\n
'''

API_RESP_BUILD_PRUNE = '''
{
  "CachesDeleted": [
    "*"
  ],
  "SpaceReclaimed": 100Mb
}\n
'''

API_RESP_IMAGES_JSON_INSPECT = '''
{
  "Id": "sha256:85f05633ddc1c50679be2b16a0479ab6f7637f8884e0cfe0f4d20e1ebb3d6e7c",
  "Container": "cb91e48a60d01f1e27028b4fc6819f4f290b3cf12496c8176ec714d0d390984a",
  "Comment": "",
  "Os": "linux",
  "Architecture": "amd64",
  "Parent": "sha256:91e54dfb11794fad694460162bf0cb0a4fa710cfa3f60979c177d920813e267c",
  "ContainerConfig": {
    "Tty": false,
    "Hostname": "e611e15f9c9d",
    "Domainname": "",
    "AttachStdout": false,
    "PublishService": "",
    "AttachStdin": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "NetworkDisabled": false,
    "OnBuild": [],
    "Image": "91e54dfb11794fad694460162bf0cb0a4fa710cfa3f60979c177d920813e267c",
    "User": "",
    "WorkingDir": "",
    "MacAddress": "",
    "AttachStderr": false,
    "Labels": {
      "com.prod.license": "Apache",
      "com.prod.version": "1.0",
      "com.prod.vendor": "Prod"
    },
    "Env": [
      "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    ],
    "Cmd": [
      "/bin/sh",
      "-c",
      "#(nop) LABEL com.corp.vendor=prod com.corp.license=GPL com.corp.version=1.0"
    ]
  },
  "DockerVersion": "1.9.0-dev",
  "VirtualSize": 188359297,
  "Size": 0,
  "Author": "",
  "Created": "2015-09-10T08:30:53.26995814Z",
  "GraphDriver": {
    "Name": "aufs",
    "Data": {}
  },
  "RepoDigests": [
    "localhost:5000/corp/busybox/app@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf"
  ],
  "RepoTags": [
    "corp:1.0",
    "corp:latest",
    "corp:stable"
  ],
  "Config": {
    "Image": "91e54dfb11794fad694460162bf0cb0a4fa710cfa3f60979c177d920813e267c",
    "NetworkDisabled": false,
    "OnBuild": [],
    "StdinOnce": false,
    "PublishService": "",
    "AttachStdin": false,
    "OpenStdin": false,
    "Domainname": "",
    "AttachStdout": false,
    "Tty": false,
    "Hostname": "e611e15f9c9d",
    "Cmd": [
      "/bin/bash"
    ],
    "Env": [
      "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    ],
    "Labels": {
      "com.prod.vendor": "Prod",
      "com.prod.version": "1.0",
      "com.prod.license": "Apache"
    },
    "MacAddress": "",
    "AttachStderr": false,
    "WorkingDir": "",
    "User": ""
  },
  "RootFS": {
    "Type": "layers",
    "Layers": [
      "sha256:1834950e52ce4d5a88a1bbd131c537f4d0e56d10ff0dd69e66be3b7dfa9df7e6",
      "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef"
    ]
  }
}
'''

API_RESP_COMMIT = '''
{
  "Hostname": "string",
  "Domainname": "string",
  "User": "string",
  "AttachStdin": false,
  "AttachStdout": true,
  "AttachStderr": true,
  "ExposedPorts": {
    "property1": {},
    "property2": {}
  },
  "Tty": false,
  "OpenStdin": false,
  "StdinOnce": false,
  "Env": [
    "string"
  ],
  "Cmd": [
    "string"
  ],
  "Healthcheck": {
    "Test": [
      "string"
    ],
    "Interval": 0,
    "Timeout": 0,
    "Retries": 0,
    "StartPeriod": 0
  },
  "ArgsEscaped": true,
  "Image": "string",
  "Volumes": {
    "property1": {},
    "property2": {}
  },
  "WorkingDir": "string",
  "Entrypoint": [
    "string"
  ],
  "NetworkDisabled": true,
  "MacAddress": "string",
  "OnBuild": [
    "string"
  ],
  "Labels": {
    "property1": "string",
    "property2": "string"
  },
  "StopSignal": "SIGTERM",
  "StopTimeout": 10,
  "Shell": [
    "string"
  ]
}
'''
