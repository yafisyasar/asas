const { error } = require('node:console');
const nodemailer = require('nodemailer');
const transporter = nodemailer.createTransport({
    service:'gmail',
    auth:{
        user:'yasaryafis@gmail.com',
        pass:'lzpnskohvnuumgjy'
    }
});
const mailOptions={
    from:'yasaryafis@gmail.com',
    to:'yasaryafis@proton.me',
    subject:'mail via nodemailer',
    text:'hi this mail is sent to you via nodemailer'
};
transporter.sendMail(mailOptions,(error,info)=>{
    if(error){
        console.log("error ",error);
    }else{
        console.log("Email sent");
        console.log("Response:",info.response);
    }
});