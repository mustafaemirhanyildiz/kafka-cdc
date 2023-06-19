# kafka-cdc
Apache Kafka ile Basit CDC Uygulaması Geliştirme Projesi

- projeyi locale klonlayın
- klasör dizinine gidip terminale "docker compose up" yazın
- 15-20 saniye bekleyin ardından MongoDB Compass'ı açın
- mongodb://localhost:27020 adresine bağlanın
- meydb adlı veri tabanını oluşturun ve kafka adlı collection'ı oluşturun
- ardınan veri tabanına veri eklediğinizde producer bu veriyi kafka server'a gönderecek
- consumuer'lar da bu verileri tüketik konsola yazdıracak

Projenin Genel Mantığı
![image](https://github.com/mustafaemirhanyildiz/kafka-cdc/assets/92929045/1e1c206f-5ba6-4069-9f8d-77d1c94c1a4c)
