import { useState } from "react";
import styled from "styled-components";

import { IoIosSearch } from "react-icons/io";

const SearchBox = () => {
  const [searchTerm, setSearchTerm] = useState(""); // 검색어 상태

  const handleSearch = (e) => {
    e.preventDefault();
    setSearchTerm(e.target.value);
    // TODO: 검색어로 검색하는 함수 호출
    console.log("검색어", searchTerm);
  };
  return (
    <Container>
      <SearchForm>
        <SearchIcon onClick={handleSearch}>
          <IoIosSearch />
        </SearchIcon>
        <SearchInput
          type="text"
          placeholder="Search..."
          value={searchTerm}
          onChange={handleSearch}
        />
      </SearchForm>
    </Container>
  );
};

export default SearchBox;

const Container = styled.div`
  display: flex;
  width: 100%;
`;

const SearchForm = styled.form`
  display: flex;
  align-items: center;
  width: 100%;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 12px 16px;
  transition: all 0.2s ease-in-out;

  &:hover {
    background: #fff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  }

  &:focus-within {
    background: #fff;
    border-color: #94a3b8;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05),
      0 0 0 3px rgba(148, 163, 184, 0.1);
  }
`;

const SearchIcon = styled.div`
  font-size: 18px;
  color: #64748b;
  margin-right: 12px;
  flex-shrink: 0;
  cursor: pointer;
`;

const SearchInput = styled.input`
  width: 100%;
  background: transparent;
  border: none;
  outline: none;
  font-size: 15px;
  line-height: 1.5;
  color: #1e293b;

  &::placeholder {
    color: #94a3b8;
    transition: opacity 0.2s ease;
  }

  &:focus::placeholder {
    opacity: 0.7;
  }
`;
