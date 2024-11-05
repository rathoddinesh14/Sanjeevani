package com.sanjeevani.jeevan;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class VitalDocumentService {
    
    @Autowired
    private VitalDocumentRepository vitalDocumentRepository;

    public List<VitalDocument> getAllVitalDocuments() {
        return vitalDocumentRepository.findAll();
    }
}
