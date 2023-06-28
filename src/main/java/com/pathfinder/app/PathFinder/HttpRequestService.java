package com.pathfinder.app.PathFinder;
import org.springframework.stereotype.Service;


import kong.unirest.Unirest;
import kong.unirest.HttpResponse;


@Service
public class HttpRequestService {

    public String makeRequest(String endpoint){
        HttpResponse<String> response = Unirest.get("http://localhost:5000/" + endpoint).asString();

        if (response.getStatus() == 200){
            return response.getBody();
        } else{
            System.out.println("Error: " + response.getStatus());
            return null;
        }
    }
    
}
