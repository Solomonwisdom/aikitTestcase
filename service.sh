rm service.zip
zip -o service.zip *
sha256sum service.zip > test.sha256sum
cat test.sha256sum
