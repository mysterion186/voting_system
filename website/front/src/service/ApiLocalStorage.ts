export default {
    saveUserStatus (status: string): void {
        window.localStorage.setItem('userStatus', status);
    },
    getUserStatus (status: string):string | null{
        return window.localStorage.getItem('userStatus')
    },

    saveUserToken(token: string): void {
        window.localStorage.setItem('userToken', token);
    },
    getUserToken (token: string):string|null{
        return window.localStorage.getItem('userToken');
    }
}