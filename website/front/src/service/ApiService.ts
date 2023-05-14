import axios, { AxiosInstance, AxiosResponse } from "axios";

const instance = axios.create({
	baseURL: process.env.REACT_APP_API_URL
});

type type_headers = {
    'Content-type' : string;
    authorization? : string;
}

export default {
    async call(method: string, ressources: string, data: object | null  = null, token : string | null = null ){
        var headers : type_headers= {
            "Content-type" : "application/json",
        };
         if (token !== null){
            headers.authorization =  "Bearer " + token;
        }
        return instance({
            method, 
            headers : headers,
            url : ressources,
            data
        }).then((response:any) => {
            return {status: response.status, data : response.data};
        }).catch((err:any) => {
            return {status: err.response.status, data : err.response.data};
        })
    },

    getLoginToken(data: {email: string, password: string}){
        return this.call("post","user/token/", data);
    },

    getCandidatesForElection(election_id:string){
        return this.call("get","vote/get-candidate/" + election_id)
    }

}