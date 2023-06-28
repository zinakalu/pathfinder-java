package com.pathfinder.app.PathFinder;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/pathfinder")
public class PathFinderController {
    private final HttpRequestService httpRequestService;

    public PathFinderController(HttpRequestService httpRequestService) {
        this.httpRequestService = httpRequestService;
    }


    @GetMapping(path="/a_star")
    public String a_star(){
        return httpRequestService.makeRequest("a_star");
    }

    @GetMapping(path="/dijkstra")
    public String dijkstra(){
        return httpRequestService.makeRequest("dijkstra");
    }

    @GetMapping(path="/bellman_ford")
    public String bellman_ford(){
        return httpRequestService.makeRequest("bellman_ford");
    }

    @GetMapping(path="/breadth_first_search")
    public String breadth_first_search(){
        return httpRequestService.makeRequest("breadth_first_search");
    }

    @GetMapping(path="/depth_first_search")
    public String depth_first_search(){
        return httpRequestService.makeRequest("depth_first_search");
    }
    
    @GetMapping(path="/floyd_warshall")
    public String floyd_warshall(){
        return httpRequestService.makeRequest("floyd_warshall");
    }
    
}
