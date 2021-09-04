import 'package:http/http.dart' as http;

Future<bool> preparationOfPrerequisitess(String input_url) async {
  //  DetectSearchPrase
  var detect_search_prase_url =
      Uri.parse('https://www.digitalbam.ir/Home/DetectSearchPrase');
  Map from = {'Phrase': input_url};
  http.Response result = await http.post(detect_search_prase_url, body: from);
  if (result == "downloadLink") {
    return true;
  } else {
    return false;
  }
}

Future<void> Generate_Link(String input_url) async {
  var generate_download_url =
      Uri.parse('https://www.digitalbam.ir/DirectLinkDownloader/Download');
  Map form = {'downloadUri': input_url};
  http.Response result = await http.post(generate_download_url, body: form);
}
