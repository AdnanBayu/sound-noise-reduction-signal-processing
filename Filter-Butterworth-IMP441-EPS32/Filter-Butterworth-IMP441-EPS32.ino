#include <driver/i2s.h>
#include <Arduino.h>

// I2S configuration
#define SAMPLE_BUFFER_SIZE 512
#define SAMPLE_RATE 10000
#define I2S_MIC_CHANNEL I2S_CHANNEL_FMT_ONLY_LEFT
#define I2S_MIC_SERIAL_CLOCK GPIO_NUM_2
#define I2S_MIC_LEFT_RIGHT_CLOCK GPIO_NUM_15
#define I2S_MIC_SERIAL_DATA GPIO_NUM_13

double xn = 0;
double xn1 = 0;
double xn2 = 0;
double yn1 = 0;
double yn2 = 0;
int k = 0;

i2s_config_t i2s_config = {
    .mode = (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_RX),
    .sample_rate = SAMPLE_RATE,
    .bits_per_sample = I2S_BITS_PER_SAMPLE_16BIT,  // Use 16-bit sample size
    .channel_format = I2S_CHANNEL_FMT_ONLY_LEFT,
    .communication_format = I2S_COMM_FORMAT_I2S,
    .intr_alloc_flags = ESP_INTR_FLAG_LEVEL1,
    .dma_buf_count = 4,
    .dma_buf_len = 1024,
    .use_apll = false,
    .tx_desc_auto_clear = false,
    .fixed_mclk = 0
};

i2s_pin_config_t i2s_mic_pins = {
    .bck_io_num = I2S_MIC_SERIAL_CLOCK,
    .ws_io_num = I2S_MIC_LEFT_RIGHT_CLOCK,
    .data_out_num = I2S_PIN_NO_CHANGE,
    .data_in_num = I2S_MIC_SERIAL_DATA
};

unsigned long startTime;
const unsigned long totalSamples = SAMPLE_RATE * 5;  // 10,000 Hz * 5 seconds = 50,000 samples
unsigned long samplesCaptured = 0;

void setup() {
  Serial.begin(115200);
  i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
  i2s_set_pin(I2S_NUM_0, &i2s_mic_pins);
  startTime = millis(); // Record the start time
}

int16_t raw_samples[SAMPLE_BUFFER_SIZE];  // 16-bit sample buffer

void loop() {
  // if (samplesCaptured >= totalSamples) {
  //   Serial.println("Recording stopped after capturing 50,000 samples.");
  //   while (true) {
  //     // Stop the loop and do nothing after capturing all samples
  //   }
  // }

  size_t bytes_read = 0;
  // Read the audio data from the I2S bus
  i2s_read(I2S_NUM_0, raw_samples, sizeof(int16_t) * SAMPLE_BUFFER_SIZE, &bytes_read, portMAX_DELAY);
  int samples_read = bytes_read / sizeof(int16_t);

  // Output the captured data (16-bit samples)
  for (int i = 0; i < samples_read; i++) {
    // Serial.println(raw_samples[i]);  // Print 16-bit samples
    xn = raw_samples[i];
    double yn = -0.493*yn1 - 0.215*yn2 + 0.427*xn + 0.854*xn1 + 0.427*xn2;
    delay(1);
    xn2 = xn1;
    yn2 = yn1;
    xn1 = xn;
    yn1 = yn;

    if(k % 3 == 0){
    // Sinyal Output Ditampilkan
    Serial.print(2*xn);
    Serial.print(" ");
    Serial.println(2*yn);
  }
  k = k+1;
    samplesCaptured++;
  }
}
