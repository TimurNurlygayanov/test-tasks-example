How To Run Selenoid + SelenoidUI + Android
------------------------------------------

Just run the following command:
```
./deploy.sh
```

How To Build Docker Android with Google Play
--------------------------------------------

1) Run script to build new android image:
```bash
git clone https://github.com/aerokube/images
cd images/selenium
sudo ./automate_android.sh
```
and choose the options for new image, for example:
```
Appium version: [1.18.1]
Android image type: google_apis_playstore
Application Binary Interface: x86
Android Version: 10.0
image tag: android10_google_play
```
1) Run docker container with new image:
```
sudo docker run -d --name emulator-test -e ENABLE_VNC=true -e SKIN=WXGA800 --privileged -p 5900:5900 -p 8888:4445 android10_google_play
```
1) Connect to VNC on localhost:5900, run Google Play service, authorize with your google account.
1) Save changes in new image:
```
sudo docker commit 08bc3cafe47b android10_google_play_authorized
```
note: 08bc3cafe47b here is the ID of docker container we started 2 steps before.
1) Now you can use this image in your browsers.json:
```
{
  "android": {
    "default": "10.0",
    "versions": {
      "10.0": {
        "image": "android10_google_play_authorized",
        "port": "4444",
        "path": "/wd/hub",
        "selenoid:options": {
          "enableVNC": true,
          "enableVideo": true,
          "enableLog": true,
          "skin": "WXGA800",
        }
      }
    }
  }
}

```
