import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;
import 'package:linknimbahakon/home/view.dart';
import 'package:url_launcher/url_launcher.dart';

class HomeLogic extends GetxController {
  String inputUrl = "";
  String downloadLink = "";
  bool loadingStatus = false;

  Future nimbahakon() async {
    loadingStatus = true;
    update();

    showSnackbar("وضعیت", "درحال آماده سازی لینک .....");

    var searchResult = await preparationOfPrerequisitess();

    if (searchResult) {
      showSnackbar("وضعیت", "درحال تولید لینک نیم بها .....");
      downloadLink = await generateLink();
      update();
      showSnackbar("موفقیت", "لینک شما آمده است!");
    } else {
      showSnackbar("خطا", "لینک وارد شده نامعتبر است");
    }

    loadingStatus = false;
    update();
  }

  Future<bool> preparationOfPrerequisitess() async {
    //  DetectSearchPrase
    var detectSearchPraseUrl =
        Uri.parse('https://www.digitalbam.ir/Home/DetectSearchPrase');
    Map from = {'Phrase': inputUrl};
    http.Response result = await http.post(detectSearchPraseUrl, body: from);

    var body = result.body;

    if (body == "downloadLink") {
      return true;
    } else {
      return false;
    }
  }

  Future<String> generateLink() async {
    String linkResult = "";

    var generateDownloadUrl =
        Uri.parse('https://www.digitalbam.ir/DirectLinkDownloader/Download');
    Map form = {'downloadUri': inputUrl};
    http.Response result = await http.post(generateDownloadUrl, body: form);

    var body = jsonDecode(result.body);

    linkResult = body['fileUrl'];

    return linkResult;
  }

  void launchGitubURL() async => await canLaunch(
          "https://github.com/mdpe-ir/link-nim-baha-kon/")
      ? await launch("https://github.com/mdpe-ir/link-nim-baha-kon/")
      : throw 'Could not launch https://github.com/mdpe-ir/link-nim-baha-kon/';

  void showSnackbar(String title, String message) {
    Get.snackbar(title, message,
        snackStyle: SnackStyle.FLOATING,
        titleText: Text(
          title,
          textAlign: TextAlign.right,
          style: kTextStyle,
        ),
        messageText: Directionality(
          textDirection: TextDirection.rtl,
          child: Text(
            message,
            textAlign: TextAlign.right,
            style: kTextStyle,
          ),
        ),
        margin: EdgeInsets.only(right: 10, bottom: 20, left: 10, top: 50));
  }
}
