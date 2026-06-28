import { useEffect, useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
} from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { router } from "expo-router";

export default function AdminDashboard() {

  const [token,setToken]=useState("");

  useEffect(()=>{

    async function loadToken(){

      const jwt=await AsyncStorage.getItem("token");

      if(!jwt){

        router.replace("/");

        return;
      }

      setToken(jwt);

    }

    loadToken();

  },[]);

  async function logout(){

    await AsyncStorage.removeItem("token");

    router.replace("/");

  }

  return(

    <View
      style={{
        flex:1,
        justifyContent:"center",
        alignItems:"center",
      }}
    >

      <Text
        style={{
          fontSize:28,
          fontWeight:"bold",
        }}
      >
        Dashboard
      </Text>

      <Text
        style={{
          marginTop:20,
          paddingHorizontal:20,
        }}
      >
        JWT Stored Successfully
      </Text>

      <Text
        numberOfLines={3}
        style={{
          margin:20,
        }}
      >
        {token}
      </Text>

      <TouchableOpacity
        onPress={logout}
        style={{
          backgroundColor:"red",
          padding:15,
          borderRadius:10,
        }}
      >
        <Text
          style={{
            color:"white",
            fontWeight:"bold",
          }}
        >
          Logout
        </Text>

      </TouchableOpacity>

    </View>

  );

}