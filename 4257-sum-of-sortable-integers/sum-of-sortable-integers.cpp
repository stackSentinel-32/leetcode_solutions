class Solution{
public:
    int sortableIntegers(vector<int>&nums){
        int n=nums.size();
        vector<int>pf_mx(n+1,0);
        vector<int>sf_mn(n+1,1e9);
        vector<int>pref_drop(n,0);

        for(int i=0;i<n;i++){
            pf_mx[i+1]=max(pf_mx[i],nums[i]);
        }

        for(int i=n-1;i>=0;i--){
            sf_mn[i]=min(nums[i],sf_mn[i+1]);
        }

        for(int i=1;i<n;i++){
            pref_drop[i]=pref_drop[i-1]+(nums[i-1]>nums[i]);
        }

        auto check=[&](int k){
            for(int st=0;st<n;st+=k){
                int end=st+k-1;
                int drops=pref_drop[end]-pref_drop[st];

                if(nums[end]>nums[st]){
                    drops++;
                }

                if(drops>1||pf_mx[st]>sf_mn[st]){
                    return false;
                }
            }

            return true;
        };

        int ans=0;

        for(int k=1;k<=n;k++){
            if(n%k==0&&check(k)){
                ans+=k;
            }
        }

        return ans;
    }
};