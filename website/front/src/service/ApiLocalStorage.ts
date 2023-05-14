export default {
    saveUserStatus (status: string): void {
        window.localStorage.setItem('userStatus', status);
    },
    getUserStatus():string | null{
        return window.localStorage.getItem('userStatus')
    },

    saveUserToken(token: string): void {
        window.localStorage.setItem('userToken', token);
    },
    getUserToken():string|null{
        return window.localStorage.getItem('userToken');
    },

    saveUserType(user_type: string): void {
        window.localStorage.setItem('userType', user_type);
    },
    getUserType():string|null{
        return window.localStorage.getItem('userType');
    }
}