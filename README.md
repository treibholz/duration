# duration

Primitive cli-script, that queries a map-provider (currently only google maps),
how long you need from A to B. With the help of
[Selenium](https://www.seleniumhq.org/) and a headless chrom(e|ium) browser.

## Usage

```
$ ./duration.py home work
Writing stupid dummy configuration to ~/.duration.yaml
From: Hauptstrasse 1, Neustadt
  To: Kirchgasse 1, Neustadt

6 Std. 20 Min.
616 km
über A6
Schnellste Route; übliche Verkehrslage
DETAILS
```
now edit ~/.duration.yaml to your needs.

### Nice defaults based on MY behaviour

If you run it with less than two arguments, or if they can't be found in
your configfile, the defaults are dynamic. (You'll be surprised!)

### Dependencies

On Debian, just type:

```sh
sudo apt-get install python3-selenium chromium-driver
```

If you use another operating-system, just install the equivalent packages.

## WTF? Why don't you just use the API?

Well, to query the API, you need an API-key with [enabled billing](https://developers.google.com/maps/documentation/distance-matrix/intro).

I just didn't want to do that for this simple, personal helper. Also this way I can share it!

On the downside, this script needs a painful lot of resources (~200MiB RAM) on your local machine, but YOLO!
