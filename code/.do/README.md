# How to Deploy the Spec
## Not tested as on 08-Jul-2022 04:08:06 - Please remove after testing
1. Install `doctl` from https://docs.digitalocean.com/reference/doctl/how-to/install/
2. Login to Digital Ocean with a token by following steps in the above doc - upto step 3
3. Check if `doctl account get` is working
4. Run `doctl create app --spec ./lisibilite-app.yaml`
