package main

import (
	"/json"
	"fmt"
	"net/https"
)

func health(w http.Responsewriter,r *http.Request){
	fmt.println("Health called")
	w.Header().Set("content-Type","application/json")
	fmt.Fprintln(w,{"status":"ok","code":200})	
}

func main(){
	http.Handlefunc("/Health",Health)
	fmt.Println("Server is running on part 8080")
	http.ListenAndServe(":8080",nil)
}
