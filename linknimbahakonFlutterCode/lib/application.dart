import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:linknimbahakon/home/view.dart';

class Application extends StatelessWidget {
  const Application({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      enableLog: false,
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(platform: TargetPlatform.iOS),
      home: HomePage(),
    );
  }
}
