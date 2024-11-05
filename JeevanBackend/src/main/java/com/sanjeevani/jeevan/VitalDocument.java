package com.sanjeevani.jeevan;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Document(collection = "mycollection")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class VitalDocument {
    private ObjectId _id;
    @Field("device_id")
    private String deviceId;
    @Field("patient_id")
    private String patientId;
    @Field("heart_rate")
    private int heartRate;
    @Field("blood_pressure")
    private BloodPressure bloodPressure;
    @Field("oxygen_level")
    private int oxygenLevel;
    private String timestamp;

    @Data
    @AllArgsConstructor
    @NoArgsConstructor
    public static class BloodPressure {
        private int systolic;
        private int diastolic;
    }
}