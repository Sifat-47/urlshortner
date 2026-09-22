package main

import(
	"fmt"
	"net/https"
)
func add(w http.Responsewriter,r *http.Request){
	fmt.Fprintln(w,"10+20=30")
}
func main(){
	http.Handlefunc("/add/",add)
	fmt.Println("Server is running on part 8080")
	http.ListenAndServe(":8080",nil)
}
 