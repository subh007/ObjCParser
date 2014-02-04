ObjCParser
==========

This is parser written in the python to parse the objectiveC header file and generate the xml equivalent of the file.

For a example we have the header file:

Sample.h
```
//
//  ViewController.h
//  NetworkAlert
//
//  Created by subh on 27/08/13.
//  Copyright (c) 2013 subh. All rights reserved.
//

#import <Foundation.h>
@interface SampleClass : NSObject<NSObject>

   @property NSDictionary *(retain) dict
   -(int)initwithnibname:(NSString *)nibname option:(NSString *)option;
@end
```
When we run our parser then it should parse the header to meaningful xml file.

Running the program :
```
$ python parser.py sample.xml
```

This program will generate the equivalend xml in the sample.xml file.
```
<?xml version="1.0"?>
<class>
  <className>SampleClass<className>
  <importLib>Foundation</importLib>
  <superClass>NSObject</superClass>
  <protocol>NSObject</protocol>
  <classVar>
    <type>int</type>
    <name>count</name>
  <classVar>
  <method>
    <methodName>
      <name>intiwithnibname:option:</name>
      <visibility>classMethod</visibility>
      <arg>
        <name>nibname</name>
        <type>int</type>
      </arg>
      <returntype>int<returntype>
    </methodName>
    <property>
      <name>data</name>
      <type>dictionary</type>
      <propAttr>retain</propAttr>
    </property>
</class>
```

NOTE : some functionalities are left remain for implementation.
