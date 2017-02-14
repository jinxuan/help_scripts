#!/bin/bash
artifact=`date |md5 | head -c8; echo`
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=$artifact -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
cd $artifact
idea .
