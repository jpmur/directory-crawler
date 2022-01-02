# File Directory Crawler

This algorithm traverses through a file system directory and outputs the contents of the directory in a JSON tree.

For example:

```json
{
  "exampleDir": [
    "exampleDir/.DS_Store",
    "exampleDir/mydoc2.txt",
    {
      "exampleDir/foobar": [
        "exampleDir/foobar/.DS_Store",
        {
          "exampleDir/foobar/foo": [
            {
              "exampleDir/foobar/foo/barbar": [
                "exampleDir/foobar/foo/barbar/exec2",
                "exampleDir/foobar/foo/barbar/mydoc.txt"
              ]
            },
            "exampleDir/foobar/foo/mydoc4.txt",
            "exampleDir/foobar/foo/mydoc3.txt",
            "exampleDir/foobar/foo/mydoc2.txt"
          ]
        },
        {
          "exampleDir/foobar/bar": [
            "exampleDir/foobar/bar/mydoc2.txt"
          ]
        }
      ]
    },
    "exampleDir/exec",
    "exampleDir/mydoc.txt"
  ]
}
```

Wherein:
- A folder is represented as an object with a single key -- the folder name, whose value is an array of its contents.
- A file is represented as a string containing its filename. 

