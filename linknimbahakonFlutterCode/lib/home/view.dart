import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:get/get.dart';

import 'logic.dart';

const kTextStyle = TextStyle(fontFamily: "Vazir");

class HomePage extends StatelessWidget {
  final logic = Get.put(HomeLogic());

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "تولید کننده ی لینک نیم بها",
          style: kTextStyle,
        ),
        actions: [
          IconButton(
              onPressed: () {
                logic.launchGitubURL();
              },
              icon: Icon(FontAwesomeIcons.github))
        ],
      ),
      body: GetBuilder<HomeLogic>(builder: (logic) {
        return Container(
          child: ListView(
            shrinkWrap: true,
            children: [
              SizedBox(height: 50),
              Text(
                "لطفا لینک خود را برای نیم بها شدن در کادر زیر وارد کنید",
                textAlign: TextAlign.center,
                style: kTextStyle.copyWith(fontSize: 18),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: CupertinoTextField(
                  style: kTextStyle.copyWith(
                    color: Colors.white,
                  ),
                  onChanged: (value) {
                    logic.inputUrl = value;
                    logic.update();
                  },
                  prefix: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Icon(FontAwesomeIcons.link),
                  ),
                  placeholder: "لینک",
                  placeholderStyle: kTextStyle.copyWith(
                    color: Colors.white.withOpacity(0.5),
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: ElevatedButton(
                  onPressed: () {
                    logic.nimbahakon();
                  },
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: logic.loadingStatus
                        ? CircularProgressIndicator(
                            color: Colors.white,
                          )
                        : Text(
                            "نیم بها کن",
                            style: kTextStyle.copyWith(fontSize: 13),
                          ),
                  ),
                ),
              ),
              Container(
                padding: EdgeInsets.all(25),
                child: Column(
                  children: [
                    Text(
                      "لینک نیم بهای شما ",
                      textAlign: TextAlign.center,
                      style: kTextStyle.copyWith(fontSize: 18),
                    ),
                    SizedBox(height: 10),
                    SelectableText(
                      logic.downloadLink,
                      textAlign: TextAlign.center,
                      style: kTextStyle.copyWith(
                          fontSize: 18, color: Colors.green),
                    ),
                  ],
                ),
              )
            ],
          ),
        );
      }),
    );
  }
}
