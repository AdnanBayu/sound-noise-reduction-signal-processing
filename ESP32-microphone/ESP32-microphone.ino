#include <driver/i2s.h>

#define I2S_WS 15        // Pin untuk Word Select (LRCL)
#define I2S_SCK 14       // Pin untuk Serial Clock (BCLK)
#define I2S_SD 32        // Pin untuk Serial Data (DOUT)

void setup() {
  Serial.begin(115200);
  
  // Konfigurasi I2S
  i2s_config_t i2s_config = {
    mode: (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_RX), // Mode master dan menerima data (RX)
    sample_rate: 16000,                               // Sample rate 16 kHz
    bits_per_sample: I2S_BITS_PER_SAMPLE_32BIT,       // Sample 32-bit
    channel_format: I2S_CHANNEL_FMT_ONLY_LEFT,        // Hanya channel kiri
    communication_format: I2S_COMM_FORMAT_I2S,        // Format komunikasi I2S standar
    intr_alloc_flags: ESP_INTR_FLAG_LEVEL1,           // Level interrupt
    dma_buf_count: 8,                                 // Jumlah buffer DMA
    dma_buf_len: 64                                   // Panjang buffer DMA
  };

  i2s_pin_config_t pin_config = {
    bck_io_num: I2S_SCK,    // Pin BCLK
    ws_io_num: I2S_WS,      // Pin LRCL
    data_in_num: I2S_SD     // Pin untuk data masuk (SD)
  };

  // Menginisialisasi I2S dengan konfigurasi yang telah diatur
  i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
  i2s_set_pin(I2S_NUM_0, &pin_config);
  i2s_zero_dma_buffer(I2S_NUM_0);
}

void loop() {
  int32_t buffer[64];
  size_t bytes_read;
  
  // Membaca data dari I2S (sensor INMP441)
  i2s_read(I2S_NUM_0, (char *)buffer, sizeof(buffer), &bytes_read, portMAX_DELAY);
  
  // Cetak data yang dibaca ke serial monitor
  // Serial.print("Data Suara: ");
  // for (int i = 0; i < 64; i++) {
  //   Serial.print(buffer[i]);
  //   Serial.print(" ");
  // }
  // Serial.println();

  // // Hanya kirim nilai numerik ke Serial Plotter
  for (int i = 0; i < 64; i++) {
    Serial.println(buffer[i]);  // Kirim setiap nilai dari buffer sebagai baris baru
  }
  
  delay(100); // Tunggu 1 detik sebelum membaca lagi
}
