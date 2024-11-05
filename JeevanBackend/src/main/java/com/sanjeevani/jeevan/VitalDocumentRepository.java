package com.sanjeevani.jeevan;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface VitalDocumentRepository extends MongoRepository<VitalDocument, String> {
    // Custom query methods if needed
}