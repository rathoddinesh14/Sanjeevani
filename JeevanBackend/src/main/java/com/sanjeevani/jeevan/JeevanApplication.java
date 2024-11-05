package com.sanjeevani.jeevan;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class JeevanApplication {

	@Autowired
	private VitalDocumentService vitalDocumentService;

	public static void main(String[] args) {
		SpringApplication.run(JeevanApplication.class, args);
	}

	@GetMapping("/hello")
	public String hello() {
		return "Hello, World!";
	}

	@GetMapping("/documents")
    public List<VitalDocument> getAllDocuments() {
        return vitalDocumentService.getAllVitalDocuments();
    }
}

