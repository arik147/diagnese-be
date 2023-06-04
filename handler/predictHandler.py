# import library
from flask import jsonify
import tensorflow as tf
import numpy as np
import json

def predictSymptom(data):
    try:
        # Define the symptoms dictionary
        my_symptom = {
            'gatal': 0,
            'ruam_kulit': 0,
            'benjolan_pada_kulit': 0,
            'bersin_bersin': 0,
            'menggigil': 0,
            'merinding': 0,
            'nyeri_sendi': 0,
            'bagian_sakit_perut': 0,
            'asam_lambung': 0,
            'sariawan': 0,
            'otot_mengecil': 0,
            'muntah': 0,
            'panas_saat_buang_air_kecil': 0,
            'keluar_darah_buang_air_kecil': 0,
            'kelelahan': 0,
            'kenaikan_berat_badan': 0,
            'anxiety': 0,
            'tangan_dan_kaki_dingin': 0,
            'perubahan_suasana_hati': 0,
            'penurunan_berat_badan': 0,
            'gelisah': 0,
            'tidak_berenergi': 0,
            'bercak_di_tenggorokan': 0,
            'kadar_gula_tidak_teratur': 0,
            'batuk': 0,
            'demam_tinggi': 0,
            'mata_cekung': 0,
            'sesak_napas': 0,
            'berkeringat': 0,
            'dehidrasi': 0,
            'gangguan_pencernaan': 0,
            'sakit_kepala': 0,
            'kulit_kekuningan': 0,
            'urine_berwarna_gelap': 0,
            'mual': 0,
            'nafsu_makan_hilang': 0,
            'nyeri_dibelakang_mata': 0,
            'sakit_punggung': 0,
            'sembelit': 0,
            'nyeri_perut': 0,
            'diare': 0,
            'demam_ringan': 0,
            'urine_menguning': 0,
            'menguningnya_mata': 0,
            'gagal_hati_akut': 0,
            'kelebihan_cairan': 0,
            'pembengkakan_perut': 0,
            'kelenjar_getah_bening_membengkak': 0,
            'tidak_enak_badan': 0,
            'penglihatan_kabur_dan_terdistorsi': 0,
            'dahak': 0,
            'iritasi_tenggorokan': 0,
            'mata_merah': 0,
            'tekanan_sinus': 0,
            'hidung_berair': 0,
            'hidung_tersumbat': 0,
            'nyeri_dada': 0,
            'anggota_tubuh_melemah': 0,
            'jantung_berdetak_cepat': 0,
            'nyeri_saat_buang_air_besar': 0,
            'nyeri_di_daerah_anus': 0,
            'tinja_berdarah': 0,
            'iritasi_di_anus': 0,
            'nyeri_leher': 0,
            'pusing': 0,
            'kram': 0,
            'memar': 0,
            'obesity': 0,
            'kaki_bengkak': 0,
            'pembuluh_darah_bengkak': 0,
            'wajah_dan_mata_bengkak': 0,
            'pembesaran_tiroid': 0,
            'kuku_rapuh': 0,
            'bengkak_ekstremitas': 0,
            'rasa_lapar_berlebihan': 0,
            'berhubungan_diluar_nikah': 0,
            'bibir_kering_dan_kesemutan': 0,
            'ucapan_tidak_jelas': 0,
            'nyeri_lutut': 0,
            'nyeri_sendi_panggul': 0,
            'otot_melemah': 0,
            'leher_kaku': 0,
            'pembengkakan_sendi': 0,
            'kaku_saat_ingin_bergerak': 0,
            'sensasi_berputar': 0,
            'kehilangan_keseimbangan': 0,
            'goyah': 0,
            'satu_sisi_tubuh_melemah': 0,
            'kehilangan_penciuman': 0,
            'ketidaknyamanan_kandung_kemih': 0,
            'bau_busuk_dari_urine': 0,
            'ingin_buang_air_kecil_terus': 0,
            'mengeluarkan_gas': 0,
            'gatal_internal': 0,
            'demam_tifoid': 0,
            'depresi': 0,
            'mudah_tersinggung': 0,
            'nyeri_otot': 0,
            'perubahan_sensorium': 0,
            'bintik_bintik_merah_di_seluruh_tubuh': 0,
            'sakit_perut': 0,
            'menstruasi_yang_tidak_normal': 0,
            'perubahan_warna_kulit_di_area_tertentu': 0,
            'air_mata_berlebih': 0,
            'peningkatan_nafsu_makan': 0,
            'air_kencing_berlebih': 0,
            'penyakit_keturunan': 0,
            'dahak_mukoid': 0,
            'dahak_sputum': 0,
            'kurangnya_konsentrasi': 0,
            'gangguan_penglihatan': 0,
            'menerima_transfusi_darah': 0,
            'menerima_suntikan_yang_tidak_steril': 0,
            'koma': 0,
            'pendarahan_perut': 0,
            'perut_kembung': 0,
            'riwayat_konsumsi_alkohol': 0,
            'dahak_berdarah': 0,
            'varises': 0,
            'jantung_berdebar': 0,
            'nyeri_saat_berjalan': 0,
            'jerawat_bernanah': 0,
            'komedo': 0,
            'menggaruk': 0,
            'pengelupasan_kulit': 0,
            'kulit_bersisik': 0,
            'celah_kecil_pada_kuku': 0,
            'peradangan_kuku': 0,
            'kulit_melepuh': 0,
            'luka_merah_di_sekitar_hidung': 0,
            'bekas_luka_berair': 0
        }

        diagnosis = [
            'AIDS',
            'Alergi',
            'Artritis',
            'Asma Bronkial',
            'Cacar air',
            'Demam berdarah',
            'Diabetes',
            'GERD',
            'Gastroenteritis',
            'Hemoroid dimorfik (ambeien)',
            'Hepatitis A',
            'Hepatitis Alkoholik',
            'Hepatitis B',
            'Hepatitis C',
            'Hepatitis D',
            'Hepatitis E',
            'Hipertensi',
            'Hipertiroidisme',
            'Hipoglikemia',
            'Hipotiroidisme',
            'Impetigo',
            'Infeksi jamur',
            'Infeksi saluran kemih',
            'Jerawat',
            'Kolestasis kronis',
            'Kuning (penyakit kuning)',
            'Malaria',
            'Migraine',
            'Osteoartritis',
            'Paralisis (pendarahan otak)',
            'Penyakit ulkus peptikum',
            'Pilek biasa',
            'Pneumonia',
            'Psoriasis',
            'Reaksi obat',
            'Serangan jantung',
            'Spondilosis Serviks',
            'Tuberculosis',
            'Typus',
            'Varises',
            'Vertigo Posisional Paroksismal'
        ]

        # Update the symptom dictionary with the received symptoms
        my_symptom.update(data)

        # Load the model
        model = tf.keras.models.load_model('model.h5')

        # Convert the symptom dictionary values to a list
        my_symptom_values = list(my_symptom.values())

        input_data = tf.convert_to_tensor([my_symptom_values], dtype=tf.float32)

        # Make predictions using the loaded model
        predictions = model.predict(input_data)

        # Print the array prediction
        # print(predictions)
        # print(predictions[0])

        # Get max value in array predictions
        # max_value = np.max(predictions[0])

        max_value_index = np.argmax(predictions[0])

        # print(diagnosis[max_value_index])

        # print(max_value)

        prediksi = diagnosis[max_value_index]
        deskripsi, dokter_spesialis = getDescriptionAndDoctor(prediksi)

        # print("Deskripsi:", deskripsi)
        # print("Rekomendasi dokter: Dokter", dokter_spesialis)

        # Return the prediction result
        return jsonify({
            'status': 'success',
            'code': 200,
            'message': 'Symptom prediction successful!',
            'data': {
                'prognosis': prediksi,
                'deskripsi': deskripsi,
                'spesialis': dokter_spesialis
            }
        })

    except Exception as e:
        print(str(e))
        return jsonify({
            'status': 'failed',
            'code': 400,
            'message': 'Error predicting symptom!'
        })
    
def getDescriptionAndDoctor(prediksi):
    # open file
    with open("glosarium.json", "r") as file:
        data = json.load(file)
        # check by label
        for item in data:
            if item['prognosis'] == prediksi:
                return item['deskripsi'], item['spesialis']
    # not found
    return "Penyakit tidak dikenali", "Tidak ada spesialis yang sesuai"