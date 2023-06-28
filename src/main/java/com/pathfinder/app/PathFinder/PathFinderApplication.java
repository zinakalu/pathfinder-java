package com.pathfinder.app.PathFinder;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class PathFinderApplication {

	public static void main(String[] args) {
		SpringApplication.run(PathFinderApplication.class, args);

		ApplicationContext applicationContext = SpringApplication.run(PathFinderApplication.class, args);
		HttpRequestService httpRequestService = applicationContext.getBean(HttpRequestService.class);

		String response = httpRequestService.makeRequest("a_star");
		System.out.println(response);
	}

}
