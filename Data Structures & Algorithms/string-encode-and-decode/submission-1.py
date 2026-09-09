class Solution:

    def encode(self, strs: List[str]) -> str | None:
        if len(strs)==0:
            return '<>'
        return "///".join(strs)

    def decode(self, s: str) -> List[str]:
        a =s.split("///")
        # print(a)
        if a==["<>"]:
            return []
        return a